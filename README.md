Динамическая Веб-страница, состоящая из:
1. Формы с текстовым полем.
2. Списком сообщений, пронумерованных с 1.

С помощью формыотправляется сообщение на сервер, где ему присваивается порядковый номер.
Далее сообщение с порядковым номером отправляется на страницу и отображается в списке.

При перезагрузке страницы данные о номерации теряются и начинается с 1.

Страница подключается к серверу по WebSocket, Взаимодействие с сервером происходит с использованием JSON
