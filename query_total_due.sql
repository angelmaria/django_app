SELECT 
    s.first_name,
    s.last_name,
    SUM(
        CASE 
            WHEN e.class_number = 1 THEN 
                p.amount  -- Primera clase, sin descuento
            WHEN e.class_number = 2 THEN 
                p.amount * 0.5  -- Segunda clase, 50% descuento
            WHEN e.class_number >= 3 THEN 
                p.amount * 0.25  -- Tercera o más, 75% descuento
            ELSE 
                p.amount  -- Default case (sin descuento)
        END * 
        (CASE 
            WHEN s.family_discount = TRUE THEN 0.9  -- Aplica un 10% de descuento adicional si hay descuento familiar
            ELSE 1  -- Sin descuento adicional
        END)
    ) AS total_amount_due
FROM 
    Student s
JOIN 
    Enrollment e ON s.id = e.student_id
JOIN 
    Class c ON e.class_id = c.id
JOIN 
    Price p ON c.price_id = p.id
GROUP BY 
    s.id, s.first_name, s.last_name
ORDER BY 
    s.last_name, s.first_name;
