# Reciclo 🌱

**Reciclo** é uma plataforma de manejo de resíduos que incentiva a reciclagem e oferece orientações de descarte adequado. Desenvolvido como um projeto educacional, o objetivo é facilitar o acesso a informações sobre reciclagem e auxiliar na localização de pontos de coleta.

---

## 🚀 Funcionalidades

- **Usuários**:
  - Acessam um mapa interativo com localização de pontos de coleta.
  - Buscam orientações de descarte com base no tipo de resíduo.
  - Consultam horários de funcionamento dos pontos de coleta.

- **Administradores**:
  - Cadastram pontos de coleta com informações detalhadas.
  - Adicionam tipos de resíduos aceitos nos pontos de coleta.

---

## 🛠️ Tecnologias Utilizadas

- **Backend**: 
  - [Python Django](https://www.djangoproject.com/)
  - Django Forms para manipulação de formulários.

- **Frontend**:
  - HTML, CSS, JavaScript.
  - [Leaflet.js](https://leafletjs.com/) para mapas interativos.

- **Mapas e Geolocalização**:
  - [OpenStreetMap](https://www.openstreetmap.org/) como base cartográfica.
  - [Nominatim API](https://nominatim.org/release-docs/latest/api/Overview/) para conversão de endereços em coordenadas geográficas.

---

## ⚙️ Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/reciclo.git
   cd reciclo
   ```
   
2. **Crie e ative o ambiente virtual:**
  ```bash
  python -m venv venv
  source venv/bin/activate  # Linux/macOS
  venv\Scripts\activate     # Windows
  ```

3. **Instale as dependências:**
  ```bash
  pip install -r requirements.txt
  ```

4. **Configure as variáveis de ambiente: crie um arquivo .env na raiz do projeto com as seguintes informações:**
  ```bash
  SECRET_KEY=your_secret_key
  DEBUG=True
  NOMINATIM_URL=https://nominatim.openstreetmap.org/search
  ```

5. **Aplique as migrações e inicie o servidor:**
  ```bash
  python manage.py migrate
  python manage.py runserver
  ```

6. **Acesse no navegador:
  ```bash
  http://127.0.0.1:8000
  ```

📦 Estrutura do Projeto
reciclo/
├── core/                   # Aplicação principal
│   ├── models.py           # Modelos de dados
│   ├── views.py            # Lógica de exibição
│   ├── forms.py            # Formulários
│   └── ...
├── templates/              # Templates HTML
├── static/                 # Arquivos estáticos (CSS, JS, imagens)
├── manage.py               # Gerenciador do Django
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo

🌍 API de Geocodificação (Nominatim)
A aplicação utiliza a API Nominatim para converter endereços em coordenadas geográficas. A integração é feita através de requisições HTTP, e os resultados são utilizados para posicionar os pontos de coleta no mapa interativo.

Exemplo de requisição:

```bash
GET https://nominatim.openstreetmap.org/search?q=Rua+Exemplo,+123&format=json
```
