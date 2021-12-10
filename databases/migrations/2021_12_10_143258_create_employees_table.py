"""CreateEmployeesTable Migration."""

from masoniteorm.migrations import Migration


class CreateEmployeesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("employees") as table:
            table.increments("id")
            table.string("name")
            table.string("position")
            table.integer("hours")
            table.integer("rate")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("employees")
