-- 코드를 입력하세요
SELECT CONCAT('/home/grep/src/', f.BOARD_ID, '/', f.FILE_ID, f.FILE_NAME, f.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE f
JOIN (
    SELECT BOARD_ID
    FROM USED_GOODS_BOARD
    WHERE VIEWS = (SELECT MAX(VIEWS)
                   FROM USED_GOODS_BOARD
                )
) b
ON f.BOARD_ID = b.BOARD_ID
ORDER BY f.FILE_ID DESC