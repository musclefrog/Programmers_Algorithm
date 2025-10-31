with DISCOUNT_PLAN as (select *
                      from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                      where DURATION_TYPE = '30일 이상'),
RENTED_NOV as (select distinct CAR_ID
              from CAR_RENTAL_COMPANY_RENTAL_HISTORY
              where START_DATE <= '2022-11-30' and END_DATE >= '2022-11-01'),
FEE_CALC as (select C.CAR_ID,
                    C.CAR_TYPE,
                    floor((C.DAILY_FEE * (1 - D.DISCOUNT_RATE / 100.0)) * 30) as FEE
            from CAR_RENTAL_COMPANY_CAR C join DISCOUNT_PLAN D
            on C.CAR_TYPE = D.CAR_TYPE
            where C.CAR_TYPE in ('세단', 'SUV'))
            
select F.CAR_ID, F.CAR_TYPE, F.FEE
from FEE_CALC F
where not exists (select 1
                 from RENTED_NOV R
                 where R.CAR_ID = F.CAR_ID)
    and F.FEE between 500000 and 1999999
order by F.FEE desc, F.CAR_TYPE, F.CAR_ID desc;