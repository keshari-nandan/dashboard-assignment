const getCubeQuery = (widget) => {
    const query = {
        measures: ['expenses.total']
    }
    applyDimension(widget, query)
    return query;
}

const applyDimension = (widget, query) => {
    switch(widget.dimension) {
        case 'cards':
            query['dimensions'] = ['cards.name']
            break;
        case 'categories':
            query['dimensions'] = ['categories.name']
            break;
        // case 'tag':
        //     query['dimensions'] = ['tags.name']
        //     break;
        case 'bank':
            query['dimensions'] = ['banks.name']
            break;
        case 'payment_mode':
            query['dimensions'] = ['expenses.payment_mode']
            break;

    }
}

export { getCubeQuery }