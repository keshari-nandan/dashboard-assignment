
import cube from '@cubejs-client/core';
import { CubeProvider as CoreCubeProvider } from '@cubejs-client/react';
const cubeApi = cube(
  'asdksahdkjashdkdashdkjas',
  { apiUrl: 'http://localhost:4000/cubejs-api/v1' }
);
const CubeProvider = ({children}) => {

    return (
        <>
            <CoreCubeProvider cubeApi={cubeApi}>
                {children}
            </CoreCubeProvider>
        </>
    );
}

export default CubeProvider;