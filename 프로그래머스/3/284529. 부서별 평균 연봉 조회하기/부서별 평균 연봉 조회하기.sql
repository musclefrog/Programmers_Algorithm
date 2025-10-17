with sub as (
    select DEPT_ID, round(avg(SAL)) as AVG_SAL
    from HR_EMPLOYEES
    group by DEPT_ID
)

select s.DEPT_ID, d.DEPT_NAME_EN, s.AVG_SAL
from HR_DEPARTMENT d join sub s
on d.DEPT_ID = s.DEPT_ID
order by AVG_SAL desc