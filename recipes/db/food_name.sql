CREATE TABLE FoodName (
       FoodNameId   INTEGER NOT NULL,
       FoodGroupId  INTEGER NOT NULL,
       FoodName     Text    NOT NULL,

       PRIMARY KEY (FoodNameId),
       FOREIGN KEY (FoodGroupId) REFERENCES FoodGroups(GroupId)
);
