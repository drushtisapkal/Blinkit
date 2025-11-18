create database blinkit;
use blinkit;
show tables;
select * from grocery_data;

select cast(sum(Total_Sales)/ 1000000 as decimal(10,2)) as Total_sales_Millions
from grocery_data
where Outlet_Establishment_year = 2022;

select cast(avg(Total_sales) as decimal(10,1)) as avg_sales from grocery_data
where Outlet_Establishment_year = 2022;
select count(*) as No_Of_Items from grocery_data
where Outlet_Establishment_year = 2022;

select cast(avg(Rating) as decimal(10,2)) as avg_Rating from grocery_data;

select  Outlet_Type, 
        cast(sum(Total_Sales) as decimal(10,2)) as Total_sales,
        CAST((SUM(Total_Sales) * 100.0 / SUM(SUM(Total_Sales)) OVER()) AS DECIMAL(10,2)) AS Sales_Percentage,
        cast(avg(Total_sales) as decimal(10,1)) as avg_sales,
        count(*) as No_Of_Items,
        cast(avg(Rating) as decimal(10,2)) as avg_Rating
from grocery_data
group by Outlet_Type
order by Total_Sales desc;


SELECT 
    Outlet_Size, 
    CAST(SUM(Total_Sales) AS DECIMAL(10,2)) AS Total_Sales,
    CAST((SUM(Total_Sales) * 100.0 / SUM(SUM(Total_Sales)) OVER()) AS DECIMAL(10,2)) AS Sales_Percentage
FROM grocery_data
GROUP BY Outlet_Size
ORDER BY Total_Sales DESC;



