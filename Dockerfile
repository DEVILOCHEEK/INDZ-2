# Вибір базового образу
FROM node:18-alpine

# Робоча директорія
WORKDIR /app

# Копіюємо package.json та package-lock.json
COPY package*.json ./

# Встановлюємо залежності
RUN npm install --production

# Копіюємо код
COPY . .

# Виставляємо порт
EXPOSE 8080

# Команда запуску додатку
CMD ["node", "index.js"]
