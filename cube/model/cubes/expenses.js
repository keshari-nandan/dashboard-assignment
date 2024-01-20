cube(`expenses`, {
  sql_table: `artica.expenses`,
  
  data_source: `default`,
  
  joins: {
    banks: {
      sql: `${CUBE}.bank_id = ${banks}.id`,
      relationship: `many_to_one`
    },
    
    cards: {
      sql: `${CUBE}.card_id = ${cards}.id`,
      relationship: `many_to_one`
    },
    
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
    
    amount: {
      sql: `amount`,
      type: `string`
    },
    
    payment_mode: {
      sql: `payment_mode`,
      type: `string`
    },
    date: {
      sql: `date`,
      type: `time`
    }
  },
  
  measures: {
    count: {
      type: `count`
    },
    total: {
      type: `sum`,
      sql: `amount`
    }
  },
  
  pre_aggregations: {
    // Pre-aggregation definitions go here.
    // Learn more in the documentation: https://cube.dev/docs/caching/pre-aggregations/getting-started
  }
});
