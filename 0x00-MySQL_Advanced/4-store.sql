-- create trigger event
DELIMITER $$
CREATE TRIGGER  update_items BEFORE INSERT ON orders
	FOR EACH ROW 
		UPDATE items SET quantity = quantity - New.number WHERE name = New.item_name;
$$
DELIMITER ;
