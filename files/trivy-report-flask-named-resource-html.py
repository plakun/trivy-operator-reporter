from flask import Flask, Response, request, render_template, jsonify
from kubernetes import client, config


app = Flask(__name__, template_folder='templates')
config.load_kube_config() # подгружаем configFile
#config.load_incluster_config() # подгружаем serviceaccount

custom_api = client.CustomObjectsApi() # Создание клиента CustomObjectsAPI
group = 'aquasecurity.github.io'  # Группа, к которой принадлежит ваш CRD
version = 'v1alpha1'

@app.route('/', methods=['GET'])
def main_page():  
    try:
        plural = 'vulnerabilityreports'      # Плюрал вашего CRD
        crd_list = custom_api.list_cluster_custom_object(group=group, version=version, plural=plural)
        name_dict = {}
        for crd in crd_list['items']:
            name_dict.update({crd["metadata"]["name"] : crd["metadata"]["namespace"]})

    except Exception as e:
        print(f'Error fetching CRDs: {e}')
    try:
        plural = 'clustercompliancereports'      # Плюрал вашего CRD
        crd_list = custom_api.list_cluster_custom_object(group=group, version=version, plural=plural)
        name_dict2 = {}
        for crd in crd_list['items']:
            name_dict2.update({crd["metadata"]["name"] : crd["metadata"]["resourceVersion"]})

    except Exception as e:
        print(f'Error fetching CRDs: {e}')
#    return jsonify(crd_list) #если нужно получить json
    return render_template('index.html', data=name_dict, data2=name_dict2)

@app.route('/get_resource', methods=['GET'])
def get_resource():
    # Получаем параметры из запроса

    plural = 'vulnerabilityreports'      # Плюрал вашего CRD
    namespace = request.args.get('namespace')
    resource_name = request.args.get('resource_name')

    # Получаем конкретный ресурс
    try:
        crd = custom_api.get_namespaced_custom_object(
            group=group,
            version=version,
            namespace=namespace,
            plural=plural,
            name=resource_name
        )
        
        data = [{
            'namespace': namespace,
            'resource_name': resource_name,
            'data': crd
        }]
#        return jsonify(crd) #если нужно получить json
        return render_template('index_vuln.html', data=data)
        
    except Exception as e:
        error = f'Error fetching CRD: {e}'
        return render_template('index_vuln.html', error=error)

@app.route('/get_report', methods=['GET'])
def get_report():
    # Получаем параметры из запроса
    plural = 'clustercompliancereports'      # Плюрал вашего CRD
    report_name = request.args.get('report_name')

    # Получаем конкретный ресурс
    try:
        crd = custom_api.get_cluster_custom_object(
            group=group,
            version=version,
            plural=plural,
            name=report_name
        )
        data = [{
            'report_name': report_name,
            'data': crd
        }]
#        return jsonify(crd) #если нужно получить json
        return render_template('index_report.html', data=data)
    
    except Exception as e:
        error = f'Error fetching CRD: {e}'
        return render_template('index_report.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)