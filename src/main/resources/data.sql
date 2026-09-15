USE JavaEE;

DELETE FROM StudentDEMS;
DELETE FROM StaffDEMS;

INSERT INTO StudentDEMS (StudentId, StudentName, Department, Password) VALUES
('20230001', '张一', '计算机学院', 'pass0001'),
('20230002', '张二', '计算机学院', 'pass0002'),
('20230003', '张三', '电子工程学院', 'pass0003'),
('20230004', '张四', '电子工程学院', 'pass0004'),
('20230005', '张五', '管理学院', 'pass0005');

INSERT INTO StaffDEMS (StaffId, StaffName, Password) VALUES
('20240001', '李一', 'pass0001'),
('20240002', '李二', 'pass0002');

UPDATE AdminDEMS SET Password = 'pass';
