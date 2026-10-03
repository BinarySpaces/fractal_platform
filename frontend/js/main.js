const API_URL = 'http://localhost:8000';

const button = document.getElementById('generate');
const result = document.getElementById('result');

button.addEventListener('click', async () => {
    button.disabled = true;
    button.textContent = 'Генерация...';
    result.innerHTML = '';

    try {
        const response = await fetch(`${API_URL}/fractal/generate`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({})
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();
        console.log(data);

        const title = document.createElement('h2');
        title.textContent = data.fractal_name;
        title.style.color = '#eee';
        title.style.marginTop = '20px';
        result.appendChild(title);

        const img = document.createElement('img');
        img.src = `${API_URL}${data.image_url}`;
        result.appendChild(img);

    } catch (error) {
        result.innerHTML = `<p style="color: red">Ошибка: ${error.message}</p>`;
    } finally {
        button.disabled = false;
        button.textContent = 'Сгенерировать фрактал';
    }
});
