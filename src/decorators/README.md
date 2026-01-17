# What is a Decorator?

## Why use one?
The decorator pattern is useful for several reasons:

Code Reusability - Apply the same logic to multiple functions without repeating code. For example, if you want timing, logging, or authentication checks on many functions, use a decorator instead of duplicating code.

Separation of Concerns - Keep your core function logic clean and separate from cross-cutting concerns (logging, caching, validation, etc.). Your function focuses on its main job, while the decorator handles auxiliary tasks.

Easy to Maintain - Change the decorator logic in one place and it automatically applies everywhere it's used, reducing bugs and maintenance overhead.

Composable - Stack multiple decorators to combine behaviors. For example:

## Use Cases
Common Use Cases:

Logging - Track function calls and results
Caching - Store results of expensive computations
Authentication/Authorization - Check permissions before execution
Rate Limiting - Control how often functions can be called
Retry Logic - Automatically retry failed function calls
Validation - Check input parameters before execution
Don't Modify Original Code - Add functionality to existing functions without changing their definition, useful when working with third-party libraries.

Instead of decorators, you'd have to either duplicate code, modify the original function (messy), or wrap calls every time you use the function (verbose).