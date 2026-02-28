/*******************************************************************************
 * @brief Circular FIFO for byte array storage implementation.
 *
 * @copyright
 * Copyright (c) 2026 FBS93.
 * See the LICENSE.md file of this project for license details.
 * This notice shall be retained in all copies or substantial portions
 * of the software.
 *
 * @warning
 * This software is provided "as is", without any express or implied warranty.
 * The user assumes all responsibility for its use and any consequences.
 ******************************************************************************/

/*******************************************************************************
 * INCLUDES
 ******************************************************************************/

/* -----------------------------------------------------------------------------
 * System library headers
 * -------------------------------------------------------------------------- */
#include <stdint.h>
#include <stdbool.h>
#include <stddef.h>

/* -----------------------------------------------------------------------------
 * External library headers
 * -------------------------------------------------------------------------- */

/* -----------------------------------------------------------------------------
 * Project-specific headers
 * -------------------------------------------------------------------------- */
#include "emf_array_fifo.h"
#include "eaf.h"

/*******************************************************************************
 * PRIVATE MACROS
 ******************************************************************************/

/*******************************************************************************
 * PRIVATE TYPEDEFS
 ******************************************************************************/

/*******************************************************************************
 * PRIVATE VARIABLES
 ******************************************************************************/

/**
 * @brief Define static file name string for asserts.
 */
EAF_DEFINE_THIS_FILE(__FILE__);

/*******************************************************************************
 * PUBLIC VARIABLES
 ******************************************************************************/

/*******************************************************************************
 * PRIVATE FUNCTIONS
 ******************************************************************************/

/* -----------------------------------------------------------------------------
 * Private function declarations
 * -------------------------------------------------------------------------- */

/* -----------------------------------------------------------------------------
 * Private function definitions
 * -------------------------------------------------------------------------- */

/*******************************************************************************
 * PUBLIC FUNCTIONS
 ******************************************************************************/

void EMF_arrayFifo_init(EMF_arrayFifo_handler_t *const handler,
                        uint8_t const n_slots,
                        uint16_t const slot_size,
                        uint8_t *const storage)
{
  EAF_ASSERT_BLOCK_BEGIN();
  EAF_ASSERT_IN_BLOCK(handler != NULL);
  EAF_ASSERT_IN_BLOCK(n_slots > 0);
  EAF_ASSERT_IN_BLOCK(slot_size > 0);
  EAF_ASSERT_IN_BLOCK(storage != NULL);
  EAF_ASSERT_BLOCK_END();

  handler->n_slots = n_slots;
  handler->slot_size = slot_size;
  handler->storage = storage;
  handler->head = 0;
  handler->tail = 0;
  handler->full = false;
}

void EMF_arrayFifo_push(EMF_arrayFifo_handler_t *const handler,
                        uint8_t const *const data)
{
  uint8_t *pdest;

  EAF_ASSERT_BLOCK_BEGIN();
  EAF_ASSERT_IN_BLOCK(handler != NULL);
  EAF_ASSERT_IN_BLOCK(data != NULL);
  EAF_ASSERT_BLOCK_END();

  if (!handler->full)
  {
    pdest = &handler->storage[handler->head * handler->slot_size];

    for (uint16_t i = 0; i < handler->slot_size; ++i)
    {
      pdest[i] = data[i];
    }

    handler->head = (uint8_t)((handler->head + 1) % handler->n_slots);

    if (handler->head == handler->tail)
    {
      handler->full = true;
    }
  }
}

void EMF_arrayFifo_pop(EMF_arrayFifo_handler_t *const handler,
                       uint8_t *const data)
{
  uint8_t *slot;

  EAF_ASSERT_BLOCK_BEGIN();
  EAF_ASSERT_IN_BLOCK(handler != NULL);
  EAF_ASSERT_IN_BLOCK(data != NULL);
  EAF_ASSERT_BLOCK_END();

  if (!EMF_arrayFifo_isEmpty(handler))
  {
    slot = &handler->storage[handler->tail * handler->slot_size];

    for (uint16_t i = 0; i < handler->slot_size; ++i)
    {
      data[i] = slot[i];
    }

    handler->tail = (uint8_t)((handler->tail + 1) % handler->n_slots);
    handler->full = false;
  }
}

void EMF_arrayFifo_peek(EMF_arrayFifo_handler_t const *const handler,
                        uint8_t *const data)
{
  uint8_t const *slot;

  EAF_ASSERT_BLOCK_BEGIN();
  EAF_ASSERT_IN_BLOCK(handler != NULL);
  EAF_ASSERT_IN_BLOCK(data != NULL);
  EAF_ASSERT_BLOCK_END();

  if (!EMF_arrayFifo_isEmpty(handler))
  {
    slot = &handler->storage[handler->tail * handler->slot_size];

    for (uint16_t i = 0; i < handler->slot_size; ++i)
    {
      data[i] = slot[i];
    }
  }
}

void EMF_arrayFifo_drop(EMF_arrayFifo_handler_t *const handler)
{
  EAF_ASSERT(handler != NULL);

  if (!EMF_arrayFifo_isEmpty(handler))
  {
    handler->tail = (uint8_t)((handler->tail + 1) % handler->n_slots);
    handler->full = false;
  }
}

void EMF_arrayFifo_flush(EMF_arrayFifo_handler_t *const handler)
{
  EAF_ASSERT(handler != NULL);

  handler->head = handler->tail = 0;
  handler->full = false;
}

bool EMF_arrayFifo_isEmpty(EMF_arrayFifo_handler_t const *const handler)
{
  EAF_ASSERT(handler != NULL);

  return (!handler->full && (handler->head == handler->tail));
}

bool EMF_arrayFifo_isFull(EMF_arrayFifo_handler_t const *const handler)
{
  EAF_ASSERT(handler != NULL);

  return handler->full;
}