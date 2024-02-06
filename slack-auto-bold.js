// Функция для форматирования текста
function formatText(text) {
    // Найти все слова перед двоеточием
    const words = text.split(/:(.+)/)[0].split(' ');
  
    // Сделать слова жирными
    const formattedWords = words.map(word => `*${word}*`).join(' ');
  
    // Вернуть форматированный текст
    return `${formattedWords}:${text.split(/:(.+)/)[1]}`;
  }
  
  // Обработчик события "onMessage"
  function onMessage(message) {
    // Проверить, содержит ли сообщение двоеточие
    if (message.text.includes(':')) {
      // Отправить форматированное сообщение
      Slack.postMessage(message.channel, formatText(message.text));
    }
  }
  
  // Подписаться на событие "onMessage"
  Slack.on('message', onMessage);
  