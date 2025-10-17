select a.APNT_NO, p.PT_NAME, p.PT_NO, d.MCDP_CD, d.DR_NAME, a.APNT_YMD
from PATIENT p, DOCTOR d, APPOINTMENT a
where a.APNT_CNCL_YN = 'N'
and DATE(a.APNT_YMD) = '2022-04-13'
and p.PT_NO = a.PT_NO
and d.MCDP_CD = 'CS'
and a.MDDR_ID = d.DR_ID
order by APNT_YMD;