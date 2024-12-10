
# PyTypes

> [!WARNING]
> PyTypes isn't currently published, please don't install it.
> If you see a package called PyTypes, then it's not that project and can be a
> malware, or an unrelated project

PyTypes is a powerful Python extension that brings TypeScript-like type safety
and additional features to Python. With PyTypes, you can enjoy enhanced type
enforcement, better code organization, and new language features that make your
Python code more robust and maintainable.

## Features

- **Transpiler and Direct interpreter**: PyTypes can be both transpiled to
  Python, or directly interpreted
- **Implicit `Any` Type**: By default, variables and functions without type
  annotations are treated as `Any`. Warnings are shown to encourage adding type annotations.
- **Selective Type Disabling**: Use decorators to disable or weaken type
  enforcement in specific parts of the code.
- **Auto Type Detection**: Use the `Auto` type to automatically detect the type at
  initialization, similar to C++'s `auto`.
- **Const**: Introduce `const` to define immutable variables.
- **Access Specifiers**: Add access specifiers like `public` (default),
  `private`, and `protected` to control access to class members.
- **Enhanced Features**: Introduce new features like `namespace` to enhance
  Python's capabilities.

## Installation

To install PyTypes, use `pip`:

> [!WARNING]
> PyTypes isn't currently published, please don't install it.
> If you see a package called PyTypes, then it's not that project and can be a
> malware, or an unrelated project

```shell
pip install ...
```

## Usage

### Basic Example

```pytypes
# Define a namespace
namespace MyNamespace:
	from pytypes import Auto, disable_type_enforcement

	# Define a class with access specifiers
	class Person:
		public name: str
		private _age: int

		def __init__(self, name: str, age: int):
			self.name = name
			self._age = age

		protected def get_age(self) -> int:
			return self._age

	# Use Auto for type detection
	def create_user(name: str, age: int) -> Auto:
		return Person(name, age)

	# Define a const variable
	const MAX_USERS = 100

# Example usage
person = MyNamespace.create_user("Alice", 25)
print(person.name)  # Output: Alice

# Disable type enforcement for a specific function
@disable_type_enforcement
def legacy_function(data):
	# Type enforcement is disabled here
	return data
```

## License

PyTypes is licensed under the [GNU General Public License v2.0](http://www.gnu.org/licenses/gpl-2.0),
see [`LICENSE`](./LICENSE) for more information.
