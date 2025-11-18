select *
from (
    select
        *,
        case
            when revenue > 20000 then 'vip'
            when revenue > 10000 then 'standart'
            else 'basic'
        end as category
    from sales
) as classified
where category = 'vip'
order by revenue desc;
