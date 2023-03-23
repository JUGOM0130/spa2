INSERT INTO
    `a_system`.`t_tree_table` (
        `tree_id`,
        `composition_id`,
        `parts_id`,
        `lv`,
        `parent_id`,
        `order`,
        `insu`,
        `bosu`
    )
VALUES
    (%s, %s, %s, %s, %s, %s, %s, %s);
