class StudentManagement:
    """
    Klasa zarzadzajaca studentami i ich ocenami.
    """
    def __init__(self):
        self.student_list = []
        self.grade_list = []
        self.add_student("student1", "Adamprzez2a", 21)
        # self.add_grade("student1", "Fizyka", 3.0)
        # self.add_student("student2", "Robert", 23)
        # self.add_grade("student2", "Fizyka", 4.0)

    def add_student(self, id: str, name: str, age: int) -> bool:
        """
        Dodaje nowego studenta do bazy danych.

        Args:
            name: Imie studenta.
            age: Wiek studenta.
            id: Unikalny identyfikator studenta.

        Returns:
            True, jesli dodanie zakonczylo sie sukcesem.
            False w przeciwnym wypadku.
        """
        if not (id, name, age):
            return False

        self.student_list.append({"id": id, "name": name, "age": age})
        return True

    def update_student(self, id: str, name: str, age: int) -> bool:
        """
        Aktualizuje dane istniejacego studenta na podstawie identyfikatora.

        Args:
            name: Imie studenta.
            age: Wiek studenta.
            id: Unikalny identyfikator studenta.

        Returns:
            True, jesli aktualizacja zakonczyla sie sukcesem.
            False w przeciwnym wypadku.
        """
        if not (id, name, age):
            return False

        for student in self.student_list:
            if student["id"] == id:
                student["name"] = name
                student["age"] = age
                return True

        return False

    def remove_student(self, id: str, ) -> bool:
        """
        Usuwa studenta z bazy danych na podstawie jego identyfikatora.

        Args:
            id: Unikalny identyfikator studenta.

        Returns:
            True, jesli usuniecie zakonczylo sie sukcesem.
            False w przeciwnym wypadku.
        """
        if not id:
            return False

        for student in self.student_list:
            if student["id"] == id:
                self.student_list.remove(student)
                return True

        return False

    def add_grade(self, student_id: str, subject: str, grade: float) -> bool:
        """
        Dodaje ocene z danego przedmiotu dla okreslonego studenta.

        Args:
            student_id: Unikalny identyfikator studenta.
            subject: Nazwa przedmiotu.
            grade: Ocena.

        Returns:
            True, jesli dodanie oceny zakonczylo sie sukcesem (2.0, 3.0, 3.5, 4.0, 4.5, 5.0),
            False w przeciwnym razie.
        """
        if not (student_id, subject, grade):
            return False

        correct_grades = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]

        if grade not in correct_grades:
            return False

# działa ale nie fajnie
        # for student in self.student_list:
        #     if student["id"] == student_id:
        #         student["grades"] = {"subject": subject, "grade": grade}
        #         print(self.student_list)
        #         return True

# nie działa ale lepiej
        # for student in self.student_list:
        #     if student["id"] == student_id:
        #         student[subject] = grade
        #         print(self.student_list)
        #         return True

        return False

    def avg_grades(self, subject: str) -> float:
        """
        Oblicza srednia ocen z danego przedmiotu dla wszystkich studentow.

        Args:
            subject: Nazwa przedmiotu.

        Returns:
            Srednia ocen z przedmiotu jako liczba zmiennoprzecinkowa.
        """
        subject_counter = 0
        grade_sum = 0
        for student in self.student_list:
            for sub in student["grades"]:
                if sub["subject"] == subject:
                    subject_counter += 1
                    grade_sum += sub["grade"]

        grade_avg = grade_sum/subject_counter

        return grade_avg
