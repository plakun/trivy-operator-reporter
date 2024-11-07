function sortTable() {
    // Получаем таблицу по ID
    const table = document.getElementById('myTable');
    const tBody = table.tBodies[0]; // Получаем тело таблицы

    // Извлекаем все строки из тела таблицы
    const rows = Array.from(tBody.querySelectorAll('tr')).slice(0); // Убираем первую строку (заголовок)
    
    // Подсчитываем количество строк и выводим в консоль
//    console.log(`Количество строк в таблице: ${rows.length}`);
    
    // Сортируем строки по приоритету
    rows.sort((a, b) => {
        const severityOrder = { CRITICAL: 5, HIGH: 4, MEDIUM: 3, LOW: 2, UNKNOWN: 1 };
        const aValue = severityOrder[a.cells[3].innerText.trim().toUpperCase()];
        const bValue = severityOrder[b.cells[3].innerText.trim().toUpperCase()];
        return bValue - aValue; // Сортировка по убыванию
    });

    // Очищаем текущий контент в теле таблицы
    tBody.innerHTML = '';

    // Добавляем отсортированные строки обратно в таблицу
    rows.forEach(row => tBody.appendChild(row));
}
