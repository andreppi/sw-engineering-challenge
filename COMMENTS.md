Code and design best practices involved:

1. Encapsulation and Separation of Concerns: Instead of directly managing JSON files within the models, I created a  dedicated class for handling database operations. This adheres to the Single Responsibility Principle.

2. DRY Principle: Avoid code repetition by creating common utility methods for repetitive tasks.

3. Error Handling: Ensure proper error handling and respondes are in place

4. File Handling: Use context managers for file operations to ensure proper resource management (i.e with).