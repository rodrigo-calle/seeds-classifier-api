# API Seed Classifications

### Models

##### Classification session

```typescript
    {    
        businessId: string;
        classificationData: {
            oocarpa: number;
            psegoustrobus: number;
            tecunumanni: number;
        };
        createdAt: number; # timestamp in seconds
        startedAt: number | null; # timestamp in seconds
        finishedAt: number | null; # timestamp in seconds
        task: {
            supplierId: string | null;
            technicalId: string | null;
            seedVarietyRequired: string | null;
            seedsVarietyLimit: number | null;
            totalSeedsLimit: string | null;
        } | null;
        userId: string;
    }
```

##### Supplier

```typescript
    {    
        businessId: string;
        createdBy: string; # userId
        HarvestMethod: string;
        Name: string;
        Phone: string;
        SeedOrigin: string;
        Email: string;
    }
```

##### Technical

```typescript
    {    
        businessId: string;
        createdBy: string; # userId
        name: string;
        phone: string;
        email: string;
        type: string;
    }
```

##### User

```typescript
    {    
      businessId: string;
      email: string;
      name: string;
      role: string;
      userId: string;
    }
```
