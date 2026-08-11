#!/usr/bin/python3
"""This module defines the Base class."""

import json
import csv
import turtle


class Base:
    """Base class for all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"

        if list_objs is None:
            list_dicts = []
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(filename, "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from a JSON file."""
        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r", encoding="utf-8") as file:
                json_string = file.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize objects to a CSV file."""
        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            if list_objs is None:
                return

            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([
                        obj.id,
                        obj.width,
                        obj.height,
                        obj.x,
                        obj.y
                    ])
            else:
                for obj in list_objs:
                    writer.writerow([
                        obj.id,
                        obj.size,
                        obj.x,
                        obj.y
                    ])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize objects from a CSV file."""
        filename = cls.__name__ + ".csv"

        try:
            with open(filename, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)

                list_dicts = []

                if cls.__name__ == "Rectangle":
                    for row in reader:
                        list_dicts.append({
                            "id": int(row[0]),
                            "width": int(row[1]),
                            "height": int(row[2]),
                            "x": int(row[3]),
                            "y": int(row[4])
                        })
                else:
                    for row in reader:
                        list_dicts.append({
                            "id": int(row[0]),
                            "size": int(row[1]),
                            "x": int(row[2]),
                            "y": int(row[3])
                        })

                return [cls.create(**d) for d in list_dicts]

        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Open a window and draw all rectangles and squares."""
        screen = turtle.Screen()
        screen.title("Rectangles and Squares")

        t = turtle.Turtle()
        t.speed(0)

        def draw_shape(x, y, width, height, color):
            t.penup()
            t.goto(x, y)
            t.pendown()

            t.fillcolor(color)
            t.pencolor("black")

            t.begin_fill()

            for _ in range(2):
                t.forward(width)
                t.right(90)
                t.forward(height)
                t.right(90)

            t.end_fill()

        for rectangle in list_rectangles:
            draw_shape(
                rectangle.x,
                rectangle.y,
                rectangle.width,
                rectangle.height,
                "skyblue"
            )

        for square in list_squares:
            draw_shape(
                square.x,
                square.y,
                square.size,
                square.size,
                "lightgreen"
            )

        t.hideturtle()
        screen.exitonclick()