
### Deletes a pet. <a name="delete"></a>

Delete a pet.

**API Endpoint**: `DELETE /pet/{petId}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `petId` | ✓ | Pet id to delete | `123` |

#### Synchronous Client

```python
from demo_api_41_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"))
res = client.pet.delete(pet_id=123)

```

#### Asynchronous Client

```python
from demo_api_41_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.pet.delete(pet_id=123)

```

### Finds Pets by status. <a name="find_by_status"></a>

Multiple status values can be provided with comma separated strings.

**API Endpoint**: `GET /pet/findByStatus`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `status` | ✗ | Status values that need to be considered for filter | `"available"` |

#### Synchronous Client

```python
from demo_api_41_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"))
res = client.pet.find_by_status()

```

#### Asynchronous Client

```python
from demo_api_41_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.pet.find_by_status()

```

### Find pet by ID. <a name="get"></a>

Returns a single pet.

**API Endpoint**: `GET /pet/{petId}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `petId` | ✓ | ID of pet to return | `123` |

#### Synchronous Client

```python
from demo_api_41_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"))
res = client.pet.get(pet_id=123)

```

#### Asynchronous Client

```python
from demo_api_41_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.pet.get(pet_id=123)

```

### Add a new pet to the store. <a name="create"></a>

Add a new pet to the store.

**API Endpoint**: `POST /pet`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `name` | ✓ |  | `"doggie"` |
| `photoUrls` | ✓ |  | `["string"]` |
| `category` | ✗ |  | `{"id": 1, "name": "Dogs"}` |
| `id` | ✗ |  | `10` |
| `status` | ✗ | pet status in the store | `"available"` |
| `tags` | ✗ |  | `[{}]` |

#### Synchronous Client

```python
from demo_api_41_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"))
res = client.pet.create(name="doggie", photo_urls=["string"], id=10)

```

#### Asynchronous Client

```python
from demo_api_41_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.pet.create(name="doggie", photo_urls=["string"], id=10)

```

### Uploads an image. <a name="upload_image"></a>

Upload image of the pet.

**API Endpoint**: `POST /pet/{petId}/uploadImage`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `data` | ✓ |  | `open("uploads/file.pdf", "rb")` |
| `petId` | ✓ | ID of pet to update | `123` |
| `additionalMetadata` | ✗ | Additional Metadata | `"string"` |

#### Synchronous Client

```python
from demo_api_41_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"))
res = client.pet.upload_image(data=open("uploads/file.pdf", "rb"), pet_id=123)

```

#### Asynchronous Client

```python
from demo_api_41_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.pet.upload_image(data=open("uploads/file.pdf", "rb"), pet_id=123)

```

#### Response

##### Type
[ApiResponse](/demo_api_41_py/types/models/api_response.py)

##### Example
`{}`

### Update an existing pet. <a name="update"></a>

Update an existing pet by Id.

**API Endpoint**: `PUT /pet`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `name` | ✓ |  | `"doggie"` |
| `photoUrls` | ✓ |  | `["string"]` |
| `category` | ✗ |  | `{"id": 1, "name": "Dogs"}` |
| `id` | ✗ |  | `10` |
| `status` | ✗ | pet status in the store | `"available"` |
| `tags` | ✗ |  | `[{}]` |

#### Synchronous Client

```python
from demo_api_41_py import Client
from os import getenv

client = Client(api_key=getenv("API_KEY"))
res = client.pet.update(name="doggie", photo_urls=["string"], id=10)

```

#### Asynchronous Client

```python
from demo_api_41_py import AsyncClient
from os import getenv

client = AsyncClient(api_key=getenv("API_KEY"))
res = await client.pet.update(name="doggie", photo_urls=["string"], id=10)

```
