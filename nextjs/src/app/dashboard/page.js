"use client";
import { useCubeQuery }  from '@cubejs-client/react';
import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { getToken } from '@/lib/auth';
import StatsWidget from '@/components/Pages/Dashboard/components/StatsWidget';

const Dashboard = () => {
    const router = useRouter();
    const [statWidgets, setStatWidgets] = useState([]);

    const dashboardWidgets = async() => {
        const token = await getToken();
        const resp = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/widgets`, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Authorization': `Bearer ${token}`
            }
        })
        const widgets = await resp.json();
        if(resp.ok) {
            const stats = widgets.filter(w => w.type === 'stats');
            setStatWidgets(stats);
        } else {
            toast.error(json.detail ?? "Could not fetch widgets");
        }
        
    }

    useEffect(() => {
        const token = localStorage.getItem('token');
        const expiredIn = localStorage.getItem('expiredIn');
        if(!token || expiredIn < Date.now()) {
            router.push('/auth/login');
        }
        dashboardWidgets().then(() => {});

    }, [])

    const { resultSet, isLoading, error, progress } = useCubeQuery({
        measures: ['expenses.total'],
        timeDimensions: [
            {
                "dimension": "expenses.date",
                "granularity": "month",
                "dateRange": "This month"
              }
        ],
        "filters": [
            {
              "member": "cards.name",
              "operator": "contains",
              "values": [
                "HDFC"
              ]
            }
          ]
      });

      if (isLoading) {
        return <div>{progress && progress.stage && progress.stage.stage || 'Loading...'}</div>;
      }
     
      if (error) {
        return <div>{error.toString()}</div>;
      }
     
      if (!resultSet) {
        return null;
      }

      const dataSource = resultSet.tablePivot();
      const columns = resultSet.tableColumns();
    return (
        <div>
            <div className="flex flex-wrap mb-4">
                {statWidgets.map((w, i) => {
                    return (
                        <StatsWidget widget={w} key={w.id} />
                    );
                })}
            </div>
        </div>
    )
}

export default Dashboard