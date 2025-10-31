-- This query is to solve cs50's fiftyville problem --

-- Find people who called that day --
SELECT p.id
FROM people as p
WHERE p.phone_number =
(
    SELECT caller
    FROM phone_calls
    WHERE month = 7
    AND day = 28
    AND duration < 60
)