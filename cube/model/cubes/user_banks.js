cube(`user_banks`, {
  sql_table: `artica.user_banks`,
  
  data_source: `default`,
  
  joins: {
    banks: {
      sql: `${CUBE}.bank_id = ${banks}.id`,
      relationship: `many_to_one`
    },
    
    users: {
      sql: `${CUBE}.user_id = ${users}.id`,
      relationship: `many_to_one`
    }
  },
  
  dimensions: {
    id: {
      sql: `id`,
      type: `number`,
      primary_key: true
    },
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
