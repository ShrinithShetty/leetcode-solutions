-- Write your PostgreSQL query statement below
select w1.id from Weather w1
join weather w2
on w1.recordDate - 1 = w2.recordDate
where w1.temperature > w2.temperature