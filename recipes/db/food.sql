CREATE TABLE Foods (
       FoodName      Text    NOT NULL,
       FoodId        INTEGER NOT NULL,
       FoodGroupId   INTEGER NOT NULL,
       calories      Real,
       protein       Real,
       fat           Real,
       carbohydrates Real,
       sugars        Real,

       PRIMARY KEY (FoodId),
       FOREIGN KEY (FoodGroupId) REFERENCES FoodGroups(GroupId)
);
