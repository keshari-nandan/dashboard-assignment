cube(`expense_tags`, {
  sql_table: `artica.expense_tags`,
  
  data_source: `default`,
  
  joins: {
    expenses: {
      sql: `${CUBE}.expense_id = ${expenses}.id`,
      relationship: `many_to_one`
    },
    
    tags: {
      sql: `${CUBE}.tag_id = ${tags}.id`,
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
