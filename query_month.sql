SELECT
	DATE_FORMAT(e.enrollment_date, '%m-%Y') AS `Mes de inscripción`,
	COUNT(*) AS `Total Inscripciones`,
	GROUP_CONCAT(DISTINCT CONCAT(s.first_name, ' ', s.last_name, ' (', sub.count_per_student, ')') ORDER BY s.last_name SEPARATOR ', ') AS `Estudiantes inscritos`
FROM
	Enrollment e
JOIN
	Student s ON e.student_id = s.id
JOIN (
	SELECT student_id, DATE_FORMAT(enrollment_date, '%m-%Y') AS enrollment_month, COUNT(*) AS count_per_student
	FROM Enrollment
	GROUP BY student_id, DATE_FORMAT(enrollment_date, '%m-%Y')
) sub ON e.student_id = sub.student_id AND DATE_FORMAT(e.enrollment_date, '%m-%Y') = sub.enrollment_month
GROUP BY
	DATE_FORMAT(e.enrollment_date, '%m-%Y')
ORDER BY
	`mes de inscripción`;