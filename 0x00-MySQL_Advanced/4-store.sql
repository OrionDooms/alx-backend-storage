-- SQL script that creates a trigger that decreases the quantity
-- of an item after adding a new order.
DELIMITER //

CREATE TRIGGER decreases_items
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET o.quantity = o.quantity - NEW.quantity
	WHERE id = NEW.item_id;
END //
DELIMITER;
