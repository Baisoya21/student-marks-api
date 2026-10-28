-- Updated Students table: one name column and marks for four subjects.
-- SQLite compatible. Run: sqlite3 students.db < students_updated.sql

DROP TABLE IF EXISTS Students;

CREATE TABLE Students (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    name     TEXT,
    roll_no  TEXT,
    maths    INTEGER,
    english  INTEGER,
    science  INTEGER,
    computer INTEGER
);

-- Marks are NULL initially because no marks were provided.
-- Enter marks for Maths, English, Science, and Computer when available.

INSERT INTO Students (name, roll_no, maths, english, science, computer) VALUES
    ('Divya Srivastava', ' 100 ', 88, 73, 84, 92),
    ('Swati Verma', '101', 84, 56, 55, 87),
    ('Varun', ' 102 ', 67,77, 78, 65),
    ('Joseph', '103', 75, 75, 64, 65),
    ('Meera Mishra', '104', 75, 63, 86, 67),
    ('Karan Saxena', '105', 89, 87, 67, 97),
    ('Arjun Dubey', '106', 66, 78, 82, 96),
    ('Mohit Verma', ' 107 ', 78, 98, 77, 92),
    ('sakshi jain', '108', 95, 78, 86, 90),
    ('Aditya TRIpAThi', '109', 94, 98, 67, 59),
    ('aditya mishra', '110', 89, 88, 59, 80),
    ('Aarti jain', '111', 94,  88, 73, 84),
    ('neha Mishra', '112', 89, 87, 67, 97),
    ('Amit Sharma', '113', 88, 73, 84, 92),
    ('Tanvi khan', '114', 89, 87, 67, 97),
    ('KARan mehta', '115', 88, 73, 84, 92),
    ('DIVYA mehta', '116', 84, 68, 71, 73),
    ('Riya Jain', ' 117 ', 75, 63, 86, 67),
    ('Divya tripathI', '118', 67,77, 78, 65),
    ('KuNal Jain', '119', 88, 73, 84, 92),
    ('abhinav Srivastava', '120', 92, 56, 60, 81),
    ('SneHa Tiwari', '121', 78, 98, 77, 92),
    ('Amit CHAUHAN', '122', 66, 60, 84, 95),
    ('Tanya Bhatia', '123', 89, 87, 67, 97),
    ('HARSH TIWARI', '124', 78, 98, 77, 92),
    ('MeerA singh', '125', 75, 63, 86, 67),
    ('Pooja Sharma', '126', 67,77, 78, 65),
    ('kUnAL PANDEY', '127', 89, 87, 67, 97),
    ('Kirti Sinha', '128',  88, 73, 84, 92),
    ('ANKIT SINGH', '129',  88, 73, 84, 92),
    ('Karan GUPTA', ' 130 ', 89, 87, 67, 97),
    ('MANISH Patel', '131', 75, 63, 86, 67),
    ('Rohit Sharma', '132', 78, 98, 77, 92),
    ('Shreya MISHRA', '133', 88, 73, 84, 92),
    ('kOMAL Jain', '134', 95, 78, 86, 90),
    ('Amit', '135', 88, 73, 84, 92),
    ('siddharth Saxena', '136', 78, 98, 77, 92),
    ('Rahul tripathi', '137', 89, 87, 67, 97),
    ('Amit CHAUHAN', '138', 95, 78, 86, 90),
    ('kArAn Saxena', '139', 78, 98, 77, 92),
    ('Mohit tiwari', '140', 88, 73, 84, 92),
    ('KARAN GUPTA', '141', 89, 87, 67, 97),
    ('ANJALi rastogi', '142', 88, 73, 84, 92);
