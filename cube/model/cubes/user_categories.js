cube(`user_categories`, {
  sql_table: `artica.user_categories`,
  
  data_source: `default`,
  
  joins: {
    categories: {
      sql: `${CUBE}.category_id = ${categories}.id`,
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
