select d.name as Department,e.name as Employee,e.salary as Salary
from employee e,department d 
where e.departmentId = d.id
and (e.departmentid,e.salary) in (select departmentid,max(salary) as max from employee group by departmentid);
