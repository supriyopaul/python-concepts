'''
Create a sophisticated Database Adapter system using Factory Method pattern with connection pooling and multiple database support.

Requirements:
- Create an abstract DatabaseAdapter class with methods:
  - `connect()`, `disconnect()`, `execute_query(query, params)`, `execute_transaction(queries)`
  - `get_connection_info()`, `health_check()`, `backup_database()`
- Implement concrete adapters for:
  - PostgreSQLAdapter: with connection pooling, prepared statements
  - MySQLAdapter: with connection pooling, transaction isolation levels
  - SQLiteAdapter: with WAL mode, foreign key constraints
  - MongoDBAdapter: with replica sets, aggregation pipelines
  - RedisAdapter: with cluster support, pub/sub capabilities
- Create a DatabaseFactory with methods:
  - `create_adapter(db_type, **connection_params)`
  - `get_adapter_registry()` - returns available adapter types
  - `register_custom_adapter(name, adapter_class)` - for extensibility
- Implement a ConnectionPool class that manages multiple connections per adapter
- Add a DatabaseManager class that:
  - Manages multiple database connections
  - Provides connection failover and load balancing
  - Implements connection health monitoring
  - Supports database migration utilities
- Include comprehensive error handling:
  - Connection timeouts and retries
  - Database-specific error mapping
  - Transaction rollback on failures
  - Pool exhaustion handling

Advanced features to implement:
- Connection string parsing for different database formats
- Automatic connection pooling based on database type
- Query result caching with TTL
- Database schema introspection
- Async/await support for non-blocking operations
- Connection encryption and SSL support
- Query performance monitoring and logging
- Database sharding support for horizontal scaling

Example usage:
```python
# Basic usage
db_factory = DatabaseFactory()
pg_adapter = db_factory.create_adapter("postgresql", 
                                      host="localhost", 
                                      port=5432, 
                                      database="myapp", 
                                      user="admin", 
                                      password="secret",
                                      pool_size=10)

# Advanced usage with manager
db_manager = DatabaseManager()
db_manager.add_connection("primary", "postgresql", connection_params)
db_manager.add_connection("replica", "postgresql", replica_params)
db_manager.add_connection("cache", "redis", redis_params)

# Failover and load balancing
result = db_manager.execute_with_failover("SELECT * FROM users", 
                                         preferred_connection="primary")

# Transaction across multiple databases
with db_manager.distributed_transaction(["primary", "cache"]) as tx:
    tx.execute("primary", "INSERT INTO users VALUES (?)", user_data)
    tx.execute("cache", "SET user:123 ?", user_cache_data)
Expected behavior:

Seamless switching between different database types
Automatic connection pooling and resource management
Robust error handling and connection recovery
Support for both SQL and NoSQL databases
Performance monitoring and query optimization hints
Thread-safe operations with proper locking mechanisms
'''