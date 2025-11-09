# 🆕 Enhanced API Features

## Flexible Field Mapping

The API now supports custom field mapping, allowing you to specify which fields to use for text content and titles.

### New Query Parameters

- `text_field` - Specify custom field name for text content
- `title_field` - Specify custom field name for titles
- `source` - Choose between `dummy`/`static` or `huggingface` data

### Auto-Detection

If custom fields aren't found, the API automatically tries these alternatives:

**Text Fields**: `content` → `plot` → `description` → `text` → `body`
**Title Fields**: `title` → `name` → `heading` → `subject`

### New Endpoint: `/data-info`

Explore available data sources and their field structures:

```bash
curl "http://localhost:8000/data-info"
```

### Usage Examples

```bash
# Default behavior (no change from before)
curl "http://localhost:8000/process"
curl "http://localhost:8000/process?type=movies"

# Use Hugging Face dataset
curl "http://localhost:8000/process?type=movies&source=huggingface"

# Custom field mapping
curl "http://localhost:8000/process?type=movies&text_field=plot&title_field=title"

# Mix custom fields with different sources
curl "http://localhost:8000/process?type=movies&source=huggingface&text_field=plot"

# Explore available data
curl "http://localhost:8000/data-info"
```

### Enhanced Response

The API now returns additional information:

```json
{
  "success": true,
  "data": {
    "type": "movies",
    "source": "huggingface",
    "count": 100,
    "fields_used": {
      "text_field": "plot",
      "title_field": "title"
    },
    "available_fields": ["id", "title", "plot", "genre", "year"],
    "texts": ["...", "..."],
    "chart_url": "http://localhost:8000/static/tsne_movies_huggingface.png"
  }
}
```

### Backward Compatibility

All existing API calls continue to work exactly as before. The new features are additive and optional.

---

**Updated: November 2025**
