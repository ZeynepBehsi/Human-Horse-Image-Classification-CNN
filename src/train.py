
# Train the model
history = model.fit(train_generator,
                    steps_per_epoch = 8,
                    epochs=15,
                    verbose = 1,
                    validation_data = validation_generator,
                    validation_steps = 8 )