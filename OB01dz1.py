# Менеджер задач

# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач

class Task:
    def __init__(self, description, deadline, is_done=False):
        self.description = description
        self.deadline = deadline
        self.is_done = is_done

    def mark_as_done(self):
        self.is_done = True

    def __str__(self):
        return f"Задача: {self.description}, Срок: {self.deadline}, {'Выполнено' if self.is_done else 'Не выполнено'}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)
        print("Задача добавлена.")

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_done()
            print("Задача отмечена как выполненная.")
        else:
            print("Задача с таким индексом не найдена.")

    def show_tasks(self):
        print("Текущие задачи:")
        for i, task in enumerate(self.tasks):
            if not task.is_done:
                print(f"{i}. {task}")


# Пример использования
if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.add_task("Почитать книгу по Python", "2023-04-25")
    task_manager.add_task("Закончить проект", "2023-05-01")

    print("\nВсе задачи после добавления:")
    task_manager.show_tasks()

    # Отмечаем первую задачу как выполненную
    task_manager.mark_task_done(0)

    print("\nТекущие задачи после отмечания одной как выполненной:")
    task_manager.show_tasks()