-- 코드를 입력하세요
SELECT DISTINCT o1.USER_ID, o1.PRODUCT_ID
FROM ONLINE_SALE o1, ONLINE_SALE o2
WHERE o1.USER_ID = o2.USER_ID
    AND o1.PRODUCT_ID = o2.PRODUCT_ID
    AND o1.SALES_DATE != o2.SALES_DATE
ORDER BY o1.USER_ID, o2.PRODUCT_ID DESC