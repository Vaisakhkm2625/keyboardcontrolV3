
# Coding conventions


`PascalCase` for **classes**,
`under_score` for **variables** and **class members**

if you use the Designer, for example, you name your button *push_button*

means a custom method my_custom_method 
internal, getWindowIcon

```python
        #Using PyQt-specific naming conventions
        self.niceLabel = QLabel("Hello, PyQt!", self)
        self.niceLabel.setGeometry(10, 10, 380, 180)

        # Using PEP 8 conventions for a custom method
        self.my_custom_method()

    def my_custom_method(self):
        print("This is a custom method.")

```

