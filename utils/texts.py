def main():
    return ('⚠️ Интервальные повторения — это научно обоснованный метод удержания в памяти, заключающаяся в '
            'повторении запомненного учебного материала по определённым, постоянно возрастающим интервалам.\n'
            '⚠️ Доказано, что использование интервального повторения повышает скорость обучения.\n\n'
            '⚠️Создайте напоминание, чтобы более продуктивно запоминать информацию')


def ask_ratio():
    return ('⌨️ Выберите вариант интервального повторения.\n\n'
            '🔸 Для расчета частоты повторений используется формула\n'
            '<b>Y = R * X + 1</b>, где\n'
            '<b>Y</b> - день повторения,\n'
            '<b>X</b> - день последнего повторения,\n'
            '<b>R</b> - коэффициент частоты повторений (обычно используется 2.5).\n\n'
            '🔸 Если R = 2.5, то дни повторений\n'
            '[1, 3, 9, 25, 64, 161, 403, ...]\n\n'
            '🔸 Если R = 2, то дни повторений\n'
            '[1, 3, 7, 15, 31, 63, 127, ...]\n\n'
            '🔸 Вы можете указать R самостоятельно.\n\n'
            'Выберите вариант 👇')


def incorrect_value():
    return (f'<code>❗️ {"Некорректные значения":^25} ❗️\n'
            f'❗️ {"Попробуйте заново":^25} ❗️</code>')


def get_text():
    return '⌨️ Введите описание (не более 150 символов):\n\n👇 ⌨️'


def get_count_day(ratio):
    return ('⌨️ Необходимо ввести количество дней, прошедших с момента изучения материала, '
            'если вы уже используете интервальное повторение для данного материала.\n\n'
            '❇️ Если вы только вчера или сегодня изучили материал, то поставьте 1\n\n'
            '🔸 Если вы изучили материал некоторое время назад, то можно поставить 2 или 3,'
            'чтобы освежить знания.\n\n'
            f'❕ Данное число будет подставлено в формулу <b>Y = {ratio} * X + 1</b> на место X.\n\n👇 ⌨️')
