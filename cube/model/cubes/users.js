cube(`users`, {
  sql_table: `artica.users`,
  
  data_source: `default`,
  
  joins: {
    
  },
  
  dimensions: {
    id: {
      sql: `id`,
      type: `number`,
      primary_key: true
    },
    
    email: {
      sql: `email`,
      type: `string`
    },
    
    first_name: {
      sql: `first_name`,
      type: `string`
    },
    
    last_name: {
      sql: `last_name`,
      type: `string`
    },
    
    created_at: {
      sql: `created_at`,
      type: `time`
    },
    
    updated_at: {
      sql: `updated_at`,
      type: `time`
    },
    
    verified_at: {
      sql: `verified_at`,
      type: `time`
    }
  },
  
  measures: {
    count: {
      type: `count`
    }
  },
  
  pre_aggregations: {
    // Pre-aggregation definitions go here.
    // Learn more in the documentation: https://cube.dev/docs/caching/pre-aggregations/getting-started
  }
});
