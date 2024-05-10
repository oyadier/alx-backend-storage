-- Creating Triggers.
CREATE Triggers qty_decrease
AFTER INSERT ON order_times
FOR EACH ROWS
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.qty_order
    WHERE item_id = NEW.item_id
END;
