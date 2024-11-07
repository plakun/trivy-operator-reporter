document.addEventListener("DOMContentLoaded", function() {
    // Получаем таблицу по ID
    const table = document.getElementById('myTable');
    
    // Перебираем все строки таблицы
    for (let i = 0; i < table.rows.length; i++) {
        let row = table.rows[i];
        
        // Проверяем, есть ли у нас столбец 'Severity'
        if (row.cells[3].innerText === 'Severity') continue; // Пропускаем строку заголовка

        // Определяем значение в колонке 'Severity' и устанавливаем соответствующий цвет фона
        switch(row.cells[3].innerText.toUpperCase()) {
            case 'LOW':
                row.cells[3].style.backgroundColor = 'green';
                break;
            case 'MEDIUM':
                row.cells[3].style.backgroundColor = 'yellow';
                break;
            case 'HIGH':
                row.cells[3].style.backgroundColor = 'orange';
                break;
            case 'CRITICAL':
                row.cells[3].style.backgroundColor = 'red';
                break;
            default:
                console.log(`Неизвестный уровень критичности: ${row.cells[3].innerText}`);
        }
        // Проверяем, есть ли у нас столбец 'Severity'
        if (row.cells[4].innerText === 'checkFail') continue; // Пропускаем строку заголовка

        // Определяем значение в колонке 'Severity' и устанавливаем соответствующий цвет фона
        switch(row.cells[4].innerText.toUpperCase()) {
            case '0':
                row.cells[4].style.backgroundColor = 'green';
                break;
            case '1':
                row.cells[4].style.backgroundColor = 'red';
                break;
            default:
                console.log(`Неизвестный уровень: ${row.cells[4].innerText}`);
        }

    }
});