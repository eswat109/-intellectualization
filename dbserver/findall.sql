select a.price, c.name, ac.value from avtomobiles a 
join avto_characteristics ac on ac.avto = a.id
join characteristics c on c.id = ac.char