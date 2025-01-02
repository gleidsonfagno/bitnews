document.addEventListener('DOMContentLoaded', function() {
    // URL da API para obter as categorias
    const apiUrl = 'http://127.0.0.1:8000/api/categories/';

    // Função para carregar as categorias da API
    function loadCategories() {
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const categoriesList = document.getElementById('categories-list');
                categoriesList.innerHTML = '';

                data.forEach(category => {
                    const li = document.createElement('li');
                    li.textContent = category.name;  // Ajuste de acordo com o campo retornado pela API
                    categoriesList.appendChild(li);
                });
            })
            .catch(error => {
                console.error('Erro ao carregar as categorias:', error);
            });
    }

    loadCategories();
});
