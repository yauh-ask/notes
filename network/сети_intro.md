Топология - это «схема» соединения компьютеров в сети.

Более строго, топология сети – конфигурация графа:
- Вершины – узлы сети (компьютеры и сетевое оборудование)
- Ребра – связи между узлами (физические или информационные)

Популярные базовые топологии компьютерных сетей:
- Полносвязная
- Ячеистая
- Кольцо
- Дерево
- Общая шина

На практике чаще всего используется смешанная топология, при которой разные сегменты сети используют разные базовые топологии.

Типы топология:
- Физическая топология – соединения устройств в сети.
- Логическая топология – правила распространения сигналов в сети.

Логическая и физическая топологии могут отличаться:
- Классический Ethernet: физическая топология звезда, а логическая - общая шина.
- Коммутируемый Ethernet: физическая топология звезда, а логическая топология полносвязная.
- Wi-Fi: проводных сеодинений между компьютерами нет, а логическая топология - общая шина.

Создание крупных компьютерных сетей – сложная задача. Для ее решения используют метод декомпозиции: разбиение крупной сложной задачи на несколько более простых. В компьютерных сетях используется композиция на уровни сети.

Базовые понятия организации компьютерных сетей:
- Сервис – описывает какие функции реализует уровень (что делает уровень).
- Протокол – правила и соглашения, используемые для связи уровня N одного компьютера с уровнем N другого компьютера (как уровень это делает).
- Интерфейс – набор примитивных операций, которые нижний уровень предоставляет верхнему (как получить доступ к уровню).

Архитектура компьютерной сети – набор уровней и протоколов сети.
Стек протоколов - Иерархически организованный набор протоколов, достаточный для организации взаимодействия по сети.
Инкапсуляция - Включение сообщения вышестоящего уровня в сообщение нижестоящего уровня.

Сообщение в компьютерных сетях состоит из трех частей: заголовок + данные + концевик (не обязателен).

Можно придумать много разных архитектур сетей и стеков протоколов, но, если мы хотим строить большие сети, которые можно объединять между собой, необходимо иметь стандарты на уровни сети, функции уровней, и протоколы, которые на них используются. Такие стандарты называются эталонными моделями компьютерных сетей. Сейчас популярны две эталонные модели:
- Модель взаимодействия открытых систем.
- Модель TCP/IP.



Модель взаимодействия открытых систем (Open Systems Interconnection) - это одна из двух популярных эталонных моделей организации компьютерных сетей. 
Модель является _юридическим стандартом_, принятым  Международной организацией по стандартизации (ISO) в 1983 г.

Модель включает 7 уровней:
1. Физический.
2. Канальный.
3. Сетевой.
4. Транспортный.
5. Сеансовый.
6. Представления.
7. Прикладной.

Кратко рассматривается назначение каждого уровня.

На практике модель OSI не используется, но с ее помощью удобно описывать, как должны быть устроены компьютерные сети.

Модель TCP/IP – одна из двух эталонных моделей организации сетей, которые популярны в настоящее время. Это фактический (de facto) стандарт на основе стека протоколов TCP/IP. Модель TCP/IP описывает, как нужно строить сети на основе разных технологий, чтобы в них работал стек TCP/IP.

Модель содержит 4 уровня:
- Сетевых интерфейсов
- Интернет
- Транспортный
- Прикладной

По назначению уровни похожи на уровни модели взаимодействия открытых систем ISO OSI. 
Уровень сетевых интерфейсов обеспечивает интеграцию стека TCP/IP с существующими сетевыми технологиями Ethernet, Wi-Fi и др. Уровень интернет (аналог сетевого уровня OSI) нужен для объединения сетей, построенных на основе разных сетевых технологий, и поиска маршрута в крупной составной сети. Транспортный уровень, как и в модели OSI, обеспечивает связь между процессами на разных компьютерах сети. 

В прикладном уровне модели TCP/IP сочетаются функции уровней сеансового, представления и прикладного модели OSI. Считается, что если приложению TCP/IP нужны возможности сеансового уровня, или уровня представления, то оно должно самостоятельно их реализовать.

Стек протоколов TCP/IP – наиболее популярный набор сетевых протоколов в настоящее время. Он является основой интернет и широко используется.
