-- Creating views.
CREATE VIEWS need_meeting
AS SELECT name from students
WHERE score=80 AND last_meeting < 1 OR > 30;